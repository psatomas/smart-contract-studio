FROM rust:1.73

# Install dependencies
RUN apt-get update && \
    apt-get install -y curl git pkg-config libudev-dev llvm clang make cmake && \
    rm -rf /var/lib/apt/lists/*

# Install Solana CLI
RUN sh -c "$(curl -sSfL https://release.anza.xyz/stable/install)"

# Add Solana CLI to PATH
ENV PATH="/root/.local/share/solana/install/active_release/bin:${PATH}"

# Install Anchor CLI
RUN cargo install --git https://github.com/coral-xyz/anchor --tag v0.27.0 anchor-cli --locked

# Set working directory
WORKDIR /workspace

# Expose Solana validator ports
EXPOSE 8899 8900 8901

# Start shell (you can manually start test-validator)
CMD ["/root/.local/share/solana/install/active_release/bin/solana-test-validator", "--reset"]