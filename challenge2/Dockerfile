# Download image
FROM node:16

# Create app directory in container
WORKDIR /usr/src/app

# Install app dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)
COPY package*.json ./

# install npm
RUN npm install
# RUN npm ci --only=production

# Copy files from current directory to container WORKDIR
COPY . .

# Set env variables in container, nodejs app will fetch that
ENV port 3000
ENV base_url conabio

# Run application
CMD [ "node", "app.js" ]