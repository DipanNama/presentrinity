<template>
    <button @click="handleClick" class="custom-button">
      Click Me
    </button>
  </template>
  
  <script setup>
  const handleClick = () => {
    alert("Button clicked!");
  };
  </script>
  
  <style scoped>
  .custom-button {
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
    background-color: #3498db;
    color: white;
    border: none;
    border-radius: 5px;
  }
  
  .custom-button:hover {
    background-color: #2980b9;
  }
  </style>
  