#!/data/data/com.termux/files/usr/bin/bash

set -e

echo "Updating packages..."
pkg update -y

echo "Installing requirements..."
pkg install -y python ffmpeg curl

if [ ! -d "$HOME/storage" ]; then
    echo "Setting up storage..."
    termux-setup-storage
fi

echo "Installing mp3split..."

curl -L \
  https://raw.githubusercontent.com/MGoosePlayZ/mp3-splitter-for-castle/main/split-mp3.py \
  -o $PREFIX/bin/mp3split

chmod +x $PREFIX/bin/mp3split

echo ""
echo "Installed successfully."
echo "Use it like:"
echo "mp3split ~/storage/music/song.mp3"
