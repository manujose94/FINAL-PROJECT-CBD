#!/bin/bash
/opt/hadoop/bin/hadoop jar /opt/hadoop/share/hadoop/tools/lib/hadoop-streaming-*.jar \
-mapper $1 \
-reducer $2 \
-file $1 \
-file $2 \
-input $3 \
-output $4