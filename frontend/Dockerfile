# Build stage
FROM node:18-alpine AS build

WORKDIR /app

# Copy dependencies files and install
COPY package.json yarn.lock ./
RUN yarn install --frozen-lockfile

# Copy all frontend source code
COPY . .

# Fix OpenSSL issue for Node
ENV NODE_OPTIONS=--openssl-legacy-provider

# Build the React app for production
RUN yarn build

# Production stage
FROM nginx:alpine

# Copy the build files from the build stage to nginx html folder
COPY --from=build /app/build /usr/share/nginx/html

# Expose port for nginx
EXPOSE 80

# Start nginx
CMD ["nginx", "-g", "daemon off;"]
