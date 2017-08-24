set style line 1 lc rgb '#0060ad' lt 1 lw 2 pt 7 ps 1.5   # --- blue
set style line 2 lc rgb '#0060ad' lt 1 lw 1 pt 7 ps 1.5   # --- blue
set offsets 0,3,2,0
set xtics 10
set ylabel "Latency (ms)"
set xlabel "No. of Concurrent Client"

plot "out.data" with lines ls 1, "out.data" using 1:2:3:4 with errorbars ls 2
