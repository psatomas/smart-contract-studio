FROM node:20-alpine

WORKDIR /app

# Copiar package.json e package-lock.json (dentro de platform_ui)
COPY platform_ui/package*.json ./

RUN npm install

# Copiar todo o código
COPY platform_ui ./

EXPOSE 5173

CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]