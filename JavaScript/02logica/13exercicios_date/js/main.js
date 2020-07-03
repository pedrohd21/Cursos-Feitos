const formulario = window.document.getElementById('form');
const data = new Date();
const dia_semana = ['Domingo', 'Segunda-Feira', 'Terça-Feria', 'Quarta-Feria', 'Quinta-Feria', 'Sexta-Feria', 'Sábado'];

const mes = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Setembro', 'Agosto', 'Outubro', 'Novembro', 'Dezembro']
formulario.innerHTML = `${dia_semana[data.getDay()]}, ${data.getDate()} de ${mes[data.getMonth()]} de ${data.getFullYear()}<br> ${data.getHours()}:${data.getMinutes()}`;

// const formulario = document.getElementById('form');
// const data = new Date();
// formulario.innerHTML = data.toLocaleDateString('pt-BR', {dateStyle: 'full', timeStyle: 'short'})