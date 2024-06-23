# Removing Existing Files
echo "Starting Tests"
echo "------------------------"

echo "Removing Existing Files"
rm -f ../data/climate_change.sqlite

if [ -f ../data/climate_change.sqlite ]; then
    echo "Failed to Remove existing output files."
    exit 1
fi

echo "Files Removed"

# Running the pipeline
echo "Running the pipeline..."
bash ./pipeline.sh

# Check the return value of pipeline.sh
if [ $? -ne 0 ]; then
    echo "pipeline.sh failed."
    exit 1
fi

echo "running system test"
python ./system-test.py

# Check the return value of system_test.sh
if [ $? -ne 0 ]; then
    echo "System Test failed."
    exit 1
fi