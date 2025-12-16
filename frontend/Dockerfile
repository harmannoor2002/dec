FROM node:18-alpine AS build
WORKDIR /app
# copy kary ga dependencies files into container
COPY package.json yarn.lock ./
# install all nodes dependencies
RUN yarn install --frozen-lockfile    

COPY . .

# Fix all problem in build process
ENV NODE_OPTIONS=--openssl-legacy-provider
# build the react app for production
RUN yarn build

# Production stage
#base image for nginx
#deploying your app to the live server (production stage)

FROM nginx:alpine

# copy the build files from the build stage to nginx html folder
COPY --from=build /app/build /usr/share/nginx/html
EXPOSE 80
#start nginx and keep it running
CMD ["nginx", "-g", "daemon off;"]
