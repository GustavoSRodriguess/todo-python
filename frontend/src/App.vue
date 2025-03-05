<template>
  <div class="app-container">
    <header class="bg-primary text-black shadow-md">
      <div class="container mx-auto px-4 py-4">
        <div class="flex justify-between items-center">
          <h1 class="text-2xl font-bold">Todo App</h1>
          <div>
            <router-link to="/" class="hover:text-white/80 mr-4">Home</router-link>
            <router-link to="/about" class="hover:text-white/80">Sobre</router-link>
          </div>
        </div>
      </div>
    </header>

    <main class="container mx-auto px-4 py-8">
      <router-view />
    </main>

    <footer class="bg-gray-100 border-t border-gray-200 mt-10">
      <div class="container mx-auto px-4 py-6 text-center text-gray-600">
        <p>Todo App &copy; {{ new Date().getFullYear() }} - Desenvolvido com Vue, Flask e Docker</p>
      </div>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
html, body {
  height: 100%;
  margin: 0;
  padding: 0;
}

.app-container {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

main {
  flex: 1;
}
</style>