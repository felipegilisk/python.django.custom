$(document).ready(function () {
  $('#valor_mensal').on('blur', function () {
      var valor = $(this).val();
      var valorFormatado = parseFloat(valor).toFixed(2);
      $(this).val(valorFormatado);
  });

  $(function () {
    $('[data-toggle="tooltip"]').tooltip()
  })
});


document.addEventListener('DOMContentLoaded', function() {
  const placaInput = document.querySelector('input[name="placa"]');

  if (placaInput != null) {
    const errorMessage = document.createElement('div');
    errorMessage.classList.add("alert");
    errorMessage.classList.add("alert-warning");

    errorMessage.role.add("alert")

    placaInput.insertAdjacentElement('afterend', errorMessage);

    placaInput.addEventListener('focusout', function(event) {
      let placa = event.target.value.toUpperCase();
      placa = placa.replace('-', ''); // Remove hífen, se presente

      // Verifica se a placa tem o formato correto
      if (/^[A-Z]{3}\d{1}[A-Z0-9]{1}\d{2}$/.test(placa)) {
        const placaFormatada = placa.replace(/^(\w{3})(\d{1})(\w{1})(\d{2})$/, '$1$2$3$4');
        placaInput.value = placaFormatada;
        errorMessage.textContent = ''; // Limpa a mensagem de erro
      } else {
        // Exibe mensagem de erro se a placa estiver incorreta
        errorMessage.textContent = 'Insira uma placa válida no formato ABC1D23';
      }
    });
  }
});