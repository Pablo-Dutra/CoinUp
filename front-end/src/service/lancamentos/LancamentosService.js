export async function getCategorias() {
    const token = sessionStorage.getItem('access_token');
    const response = await axios.get('http://127.0.0.1:8000/categoria', {
        headers: {
            accept: 'application/json',
            Authorization: `Bearer ${token}`
        }
    });
    return response.data;
}

export async function getTipoContas() {
    const token = sessionStorage.getItem('access_token');
    const response = await axios.get('http://127.0.0.1:8000/tipoconta', {
        headers: {
            accept: 'application/json',
            Authorization: `Bearer ${token}`
        }
    });
    return response.data;
}

export async function getContas() {
    const token = sessionStorage.getItem('access_token');
    const response = await axios.get('http://127.0.0.1:8000/conta', {
        headers: {
            accept: 'application/json',
            Authorization: `Bearer ${token}`
        }
    });
    return response.data;
}

export async function getTipoTransacoes() {
    const token = sessionStorage.getItem('access_token');
    const response = await axios.get('http://127.0.0.1:8000/tipotransacao', {
        headers: {
            accept: 'application/json',
            Authorization: `Bearer ${token}`
        }
    });
    return response.data;
}
import axios from 'axios';
import formataData from '@/helpers/formataData';
import formataValor from '@/helpers/formataValor';

export async function getLancamentos(params) {
    const token = sessionStorage.getItem('access_token');
    const response = await axios.get('http://127.0.0.1:8000/lancamentos', {
        headers: {
            accept: 'application/json',
            Authorization: `Bearer ${token}`
        },
        params: params
    });
    // Aplica formatação nos dados
    return response.data.map(lancamento => ({
        ...lancamento,
        dataLancamento: formataData(lancamento.dataLancamento),
        dataTransacao: formataData(lancamento.dataTransacao),
        valorFormatado: formataValor(lancamento.valor)
    }));
}
