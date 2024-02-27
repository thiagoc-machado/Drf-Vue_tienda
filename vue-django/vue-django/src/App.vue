<template>
    <div class="container my-4">
        <h1 class="text-primary">{{ titulo }}</h1>
        <h3 class="test-secundary">Probando vue</h3>
        <h3 v-bind:class="textWarning">Probando vue com v-bind</h3>
        <h3 :class="textInfo">Probando vue com v-bind simplificado</h3>

        <h3>
          {{ estado ? "el estado es verdadero (opr. ternario)" : "el estado es falso" }}
        </h3>

        <h3 v-if="estado">El estado es verdadero {usando v-if}</h3>
        <h3 v-else>El estado es falso {usando v-else}</h3>
    </div>
</template>

<script setup>
const titulo = "vue3";
const textWarning = "text-warning";
const textInfo = "text-info";

const estado = false;
</script>

<style></style>
