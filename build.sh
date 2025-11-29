#!/bin/bash

cd backend

# Remove old venv and create new one
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip install .

# Build Go executable
cd api
rm -f api
go build -o api api.go

cd ../..
echo "Build complete"