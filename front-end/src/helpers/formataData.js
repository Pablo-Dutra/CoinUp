export default function formataData(isoString) {
    if (!isoString) return '';
    const [ano, mes, dia] = isoString.substring(0, 10).split('-');
    return `${dia}/${mes}/${ano}`;
}
