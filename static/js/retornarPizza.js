// Função para buscar os sabores do backend
async function carregarSabores() {
    const response = await fetch('/get_sabores');
    const sabores = await response.json();
    console.log("Sabores carregados:", sabores);  // Adicione esse log
  
    const selectElement = document.getElementById('pizza-select');
  
    // Adiciona cada sabor como uma opção no select
    sabores.forEach(sabor => {
      const option = document.createElement('option');
      option.value = sabor;
      option.textContent = sabor;
      selectElement.appendChild(option);
    });
  }
  
  // Carregar os sabores assim que a página for carregada
  document.addEventListener('DOMContentLoaded', carregarSabores);  