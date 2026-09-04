name: Build APK with Buildozer

on:
  push:
    branches:
      - main
  workflow_dispatch:

jobs:
  build:
    name: Build Android APK
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.10"

      - name: Install system dependencies
        run: |
          sudo apt-get update
          sudo apt-get install -y \
            git zip unzip wget curl openjdk-17-jdk \
            autoconf automake libtool pkg-config cmake \
            gettext libffi-dev libssl-dev zlib1g-dev \
            libsqlite3-dev libbz2-dev liblzma-dev \
            libreadline-dev libgdbm-dev libncurses-dev \
            libgl-dev libgles2-mesa-dev ccache

      - name: Install Buildozer
        run: |
          python -m pip install --upgrade pip
          python -m pip install "buildozer>=1.5.0" "cython<3.0"

      - name: Build APK
        run: |
          buildozer -v android debug

      - name: Upload APK artifact
        uses: actions/upload-artifact@v4
        with:
          name: SmartRisk-App
          path: bin/*.apk
