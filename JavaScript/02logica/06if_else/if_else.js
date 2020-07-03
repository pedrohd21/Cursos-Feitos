const nota1 = 0;
const nota2 = 7;
const nota3 = 8;
const nota4 = 7;

const media = (nota1 + nota2 + nota3 + nota4) / 4;

if (media >= 7) {
    console.log(`Media: ${media.toFixed(2)} Aprovado`);
} else if (media >= 5) {
    console.log(`Media: ${media.toFixed(2)} Recuperação`);
} else {
    console.log(`Media: ${media.toFixed(2)} Reprovado`);
}