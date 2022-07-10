
#!/bin/bash
for i in {1..102};
do echo "Loop $i";
RES=$(python3 try.py);
echo "${RES}," >> iss-dump.txt;
sleep 10;
done 