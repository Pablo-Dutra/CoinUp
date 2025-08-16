<template>
    <div class="card">
        <Toast />
        <div class="font-semibold text-xl mb-4"><i class="pi pi-dollar"></i> Lançamentos</div>
        <div class="flex gap-4 mb-4">
            <div>
                <label for="dataInicial" class="block text-sm font-medium text-gray-400">Data Inicial</label>
                <input type="date" id="dataInicial" v-model="dataInicial" @change="buscarLancamentos" class="border rounded px-2 py-1" />
            </div>
            <div>
                <label for="dataFinal" class="block text-sm font-medium text-gray-400">Data Final</label>
                <input type="date" id="dataFinal" v-model="dataFinal" @change="buscarLancamentos" class="border rounded px-2 py-1" />
            </div>
        </div>
        <DataTable 
            :value="lancamentos" 
            rowGroupMode="subheader" 
            stripedRows 
            groupRowsBy="dataTransacao" 
            sortMode="single" 
            sortField="dataTransacao" 
            :sortOrder="8" 
        >
            <template #groupheader="slotProps">
                <div class="flex items-center gap-2 group-header-right">
                    <span class="group-header-small">Data: {{ slotProps.data.dataTransacao }}</span>
                </div>
            </template>
            <Column field="descricao" header="Descrição" sortable />
            <Column field="categoria_descricao" header="Categoria" sortable />
            <Column field="conta_nome" header="Conta" sortable />
            <Column field="tipoconta_descricao" header="Tipo" sortable />
            <Column field="tipotransacao_descricao" header="Natureza" sortable />
            <Column field="dataLancamento" header="Lançamento" sortable />
            <Column field="dataTransacao" header="Data Transação" sortable />
            <Column field="valorFormatado" header="Valor" sortable />
        </DataTable>
        <div class="flex items-center gap-2 group-header-right p-2 m-2">
            <span class="total">Saldo {{ formataValor(total) }}</span>
        </div>
    </div>
</template>

<script setup>
import { onBeforeMount, ref } from 'vue';
import { useToast } from 'primevue/usetoast';
import { getLancamentos } from '../../../service/lancamentos/LancamentosService';
import formataValor from '@/helpers/formataValor';

const lancamentos = ref([]);
const total = ref(0);
const toast = useToast();

const hoje = new Date();
const primeiroDia = new Date(hoje.getFullYear(), hoje.getMonth(), 1);
const ultimoDia = new Date(hoje.getFullYear(), hoje.getMonth() + 1, 0);

function formatDate(date) {
    return date.toISOString().split('T')[0];
}

const dataInicial = ref(formatDate(primeiroDia));
const dataFinal = ref(formatDate(ultimoDia));

async function buscarLancamentos() {
    try {
        const params = {
            dataInicial: dataInicial.value,
            dataFinal: dataFinal.value
        };
        lancamentos.value = await getLancamentos(params);
        total.value = lancamentos.value.reduce((acc, element) => {
            const valorNum = Number(element.valor);
            return acc + (isNaN(valorNum) ? 0 : valorNum);
        }, 0);
    } catch (err) {
        if (err.response && err.response.status === 401) {
            toast.add({
                severity: 'error',
                summary: 'Não autorizado',
                detail: 'Usuário não autorizado',
                life: 3000
            });
        }
        console.error('Erro ao buscar lançamentos:', err);
    }
}

onBeforeMount(() => {
    buscarLancamentos();
});
</script>
<style scoped lang="scss">
:deep(.p-datatable-frozen-tbody) {
    font-weight: bold;
}
:deep(.p-datatable-scrollable .p-frozen-column) {
    font-weight: bold;
}
 .group-header-small {
    font-size: 0.85rem;
    font-weight: 700;
    color: #a1a1a1;
 }
 .total {
    font-size: 1.5rem;
    color: #ffffff;
 }

.group-header-right {
    justify-content: flex-end;
    width: 100%;
}
</style>
