echo "Removing old container..."
bash remove.sh 
echo "Building new container..."
bash build.sh
echo "Starting up new container..."
bash run.sh

echo "New instance running!"
