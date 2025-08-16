export default function formataValor(valor) {
    if (typeof valor !== 'number') return '';
    return (
        'R$ ' + valor
            .toFixed(2)
            .replace('.', ',')
            .replace(/\B(?=(\d{3})+(?!\d))/g, '.')
    );
}
