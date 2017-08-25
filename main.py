#! /usr/bin/python

import os
import subprocess
import csv

URL = 'http://localhost:8080/'
REQUESTS = 5000

FNULL = open(os.devnull, 'w')

class Result(object):
    def __init__(self, num_clients):
        self.num_clients = num_clients
        self.mean = None
        self.low = None
        self.high = None

    def __str__(self):
        return '%d %f %f %f' % (
                self.num_clients, 
                self.mean,
                self.low,
                self.high)

def run(num_clients):
    print 'running test with', num_clients, 'clients...'
    file_name = "%s.csv" % (num_clients)
    subprocess.check_call([
        "ab",
        "-c %d " % (num_clients),
        "-n %d" % (REQUESTS),
        "-e%s" % (file_name),
        URL
        ], stdout=FNULL)
    return file_name

def warmup():
    print 'warming up server...'
    subprocess.check_call([
        "ab",
        "-c %d " % 10,
        "-n %d" % (10000),
        URL
        ], stdout=FNULL)


def main():
    # warmup the server
    warmup()

    tests = [1, 5, 10, 20, 50, 100]
    results = {}

    for t in tests:
        results[t] = run(t)

    out = {}
    for num_client, file_name in results.iteritems():
        out[num_client] = Result(num_client)
        with open(file_name) as file:
            # consume info line
            file.readline()
            csv_reader = csv.reader(file)
            for row in csv_reader:
                percentile = int(row[0])
                latency = float(row[1])

                if percentile == 50:
                    out[num_client].mean = latency
                if percentile == 20:
                    out[num_client].low = latency
                if percentile == 80:
                    out[num_client].high = latency
        # remove file, we don't need it anymore
        os.remove(file_name)

    with open('out.data', 'w') as f:
        for t in tests:
            f.write(str(out[t]))
            f.write('\n')

if __name__ == '__main__':
    main()
