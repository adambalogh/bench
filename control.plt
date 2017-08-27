set style line 1 lc rgb '#0060ad' lt 1 lw 2 pt 5 ps 1

set style line 3 lc rgb '#660000' lt 1 lw 2 pt 7 ps 1

set style line 5 lc rgb '#009900' lt 1 lw 2 pt 3 ps 1

set offsets 0,4,4,0
set xtics 20
set ylabel "Latency (ms)" font "Charter, 17"
set xlabel "No. of Concurrent Requests" font "Charter,17"

set border

set key on outside center right

set grid ytics
set tic scale 0
set grid ytics lc rgb "#505050"

set terminal aqua title "Benchmark" font "Charter,14"  

# plot "baseline.data" with linespoints ls 1 title "Baseline", "sleuth.data" with linespoints ls 5 title "Sleuth", "microtrace.data" with linespoints ls 3 title "MicroTrace"

plot "baseline.data" with errorbar ls 1 title "", "baseline.data" with lines ls 1 title "Baseline"

