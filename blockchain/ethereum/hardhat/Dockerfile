# Use official Node.js LTS image
FROM node:22

# Set working directory
WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the project
COPY . .

# Expose default HardHat port
EXPOSE 8545

# Default command to start HardHat node
CMD ["npx", "hardhat", "node"]