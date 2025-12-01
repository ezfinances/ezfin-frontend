# Build stage
FROM node:18-alpine AS build
WORKDIR /app

# Install dependencies first (cache)
COPY package.json package-lock.json* ./
RUN npm install

# Copy source and build
COPY . .

# Build com variáveis de ambiente (use default se não fornecido)
ARG REACT_APP_API_URL=http://localhost:8000
ENV REACT_APP_API_URL=$REACT_APP_API_URL
RUN npm run build

# Production stage - serve with nginx
FROM nginx:stable-alpine

# Remove default nginx content
RUN rm -rf /usr/share/nginx/html/*

# Copy nginx configuration
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Copy built static files from build stage
COPY --from=build /app/build /usr/share/nginx/html

# Create a non-root user for nginx
RUN chown -R nginx:nginx /usr/share/nginx/html

# Expose port 80
EXPOSE 80

# Start nginx in foreground
ENTRYPOINT ["/bin/sh", "-c", "exec nginx -g 'daemon off;'"]
