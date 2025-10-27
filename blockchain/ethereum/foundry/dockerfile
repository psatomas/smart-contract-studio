# Use Ubuntu as base
FROM ubuntu:22.04

# Install dependencies
RUN apt-get update && apt-get install -y \
    curl \
    git \
    build-essential \
    libssl-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Install Foundry (forge, cast, anvil)
RUN curl -L https://foundry.paradigm.xyz | bash && \
    /root/.foundry/bin/foundryup

# Add Foundry to PATH
ENV PATH="/root/.foundry/bin:${PATH}"

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Copy start script
COPY start.sh /app/start.sh
RUN chmod +x /app/start.sh

# Default command
CMD ["/app/start.sh"]