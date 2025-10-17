#!/bin/bash
echo "🛠️  Starting Foundry environment..."

# Show forge version
forge --version
cast --version

# Automatically build the project
forge build

# Run tests
forge test

# Drop into interactive shell
echo "✅ Environment ready. Dropping into bash..."
exec /bin/bash
