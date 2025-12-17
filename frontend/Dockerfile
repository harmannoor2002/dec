# Use Node image
FROM node:16-alpine

# Set working directory
WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy frontend source code
COPY . .

# Build frontend
RUN npm run build

# Expose frontend port
EXPOSE 3000

# Start frontend
CMD ["npm", "start"]
