#!/bin/bash
echo "Running the pipeline..."
jv ./climate_change.jv -d

# Check the return value of pipeline.sh
if [ $? -ne 0 ]; then
    echo "pipeline.sh failed."
    exit 1
fi