#!/bin/bash
find . -type f -name "*.md" -exec sed -i '/{{IDE/d' {} +
find . -type f -name "*.md" -exec sed -i "s/\?\?\?/???+/g" {} +
find . -type f -name "*.md" -exec sed -i "s/\!\!\!/!!!+/g" {} +