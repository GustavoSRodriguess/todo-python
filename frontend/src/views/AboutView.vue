<template>
  <div class="about">
    <div class="card max-w-3xl mx-auto">
      <h1 class="text-2xl font-bold mb-4">Sobre o Todo App</h1>
      
      <p class="mb-4">
        Este é um aplicativo de lista de tarefas desenvolvido com tecnologias modernas para aprendizado.
      </p>
      
      <h2 class="text-xl font-semibold mt-6 mb-2">Tecnologias Utilizadas</h2>
      
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div class="card bg-gray-50 p-4">
          <h3 class="font-bold text-lg mb-2">Frontend</h3>
          <ul class="list-disc pl-5 space-y-1">
            <li>Vue.js 3 (Composition API)</li>
            <li>Tailwind CSS</li>
            <li>Vue Router</li>
            <li>Axios</li>
          </ul>
        </div>
        
        <div class="card bg-gray-50 p-4">
          <h3 class="font-bold text-lg mb-2">Backend</h3>
          <ul class="list-disc pl-5 space-y-1">
            <li>Python Flask</li>
            <li>SQLAlchemy ORM</li>
            <li>PostgreSQL</li>
            <li>RESTful API</li>
          </ul>
        </div>
      </div>
      
      <div class="card bg-gray-50 p-4 mt-4">
        <h3 class="font-bold text-lg mb-2">DevOps</h3>
        <ul class="list-disc pl-5 space-y-1">
          <li>Docker</li>
          <li>Docker Compose</li>
          <li>Ambiente de desenvolvimento containerizado</li>
        </ul>
      </div>
      
      <div class="mt-8">
        <p class="text-gray-600">
          Este projeto foi criado como exemplo de aplicação full-stack moderna.
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AboutView'
}
</script>