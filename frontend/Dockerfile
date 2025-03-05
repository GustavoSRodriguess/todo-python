FROM node:18-alpine

WORKDIR /app

# Instalar dependências
COPY package.json ./
RUN npm install

# Copiar o código-fonte
COPY . .

# Exposição da porta
EXPOSE 8080

# Comando para iniciar em desenvolvimento
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]