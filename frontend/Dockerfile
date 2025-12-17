# Build stage
FROM node:18-alpine AS build

WORKDIR /app

# Copy dependencies files and install
COPY package.json yarn.lock ./
RUN yarn install --frozen-lockfile

<<<<<<< HEAD
# Copy all frontend source code
=======
# Copy source code
>>>>>>> b3cfc5f (Fix Dockerfile merge conflicts)
COPY . .

# Fix OpenSSL issue for Node
ENV NODE_OPTIONS=--openssl-legacy-provider

<<<<<<< HEAD
# Build the React app for production
=======
# Build React app for production
>>>>>>> b3cfc5f (Fix Dockerfile merge conflicts)
RUN yarn build

# Production stage
FROM nginx:alpine

<<<<<<< HEAD
# Copy the build files from the build stage to nginx html folder
COPY --from=build /app/build /usr/share/nginx/html

# Expose port for nginx
=======
# Copy build files from build stage to nginx html folder
COPY --from=build /app/build /usr/share/nginx/html

>>>>>>> b3cfc5f (Fix Dockerfile merge conflicts)
EXPOSE 80

# Start nginx
CMD ["nginx", "-g", "daemon off;"]
