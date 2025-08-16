<template>
    <div class="card">
        <Toast />
        <div class="font-semibold text-xl mb-4"><i class="pi pi-dollar"></i> Lançamentos</div>
        <Accordion :activeIndex="0" expandIcon="pi pi-plus" collapseIcon="pi pi-minus">
            <AccordionTab>
                <template #header>
                    <span class="flex align-items-center gap-2 w-full">
                        <span class="font-bold white-space-nowrap">Filtros</span>
                    </span>
                </template>
                <div class="flex gap-4 mb-4">
                    <div>
                        <label for="dataInicial" class="block text-sm font-medium text-gray-400">Data Inicial</label>
                        <input type="date" id="dataInicial" v-model="dataInicial" @change="buscarLancamentos" class="border rounded px-2 py-1" />
                    </div>
                    <div>
                        <label for="dataFinal" class="block text-sm font-medium text-gray-400">Data Final</label>
                        <input type="date" id="dataFinal" v-model="dataFinal" @change="buscarLancamentos" class="border rounded px-2 py-1" />
                    </div>
                    <div>
                        <label for="categoria" class="block text-sm font-medium text-gray-400">Categoria</label>
                        <select id="categoria" v-model="categoriaSelecionada" @change="buscarLancamentos" class="border rounded px-2 py-1 w-40">
                            <option value="" selected>Todas</option>
                            <option v-for="cat in categorias" :key="cat.id" :value="cat.id">{{ cat.descricao }}</option>
                        </select>
                    </div>
                    <div>
                        <label for="tipoConta" class="block text-sm font-medium text-gray-400">Tipo Conta</label>
                        <select id="tipoConta" v-model="tipoContaSelecionada" @change="buscarLancamentos" class="border rounded px-2 py-1 w-40">
                            <option value="" selected>Todos</option>
                            <option v-for="tipo in tipoContas" :key="tipo.id" :value="tipo.id">{{ tipo.descricao }}</option>
                        </select>
                    </div>
                    <div>
                        <label for="conta" class="block text-sm font-medium text-gray-400">Conta</label>
                        <select id="conta" v-model="contaSelecionada" @change="buscarLancamentos" class="border rounded px-2 py-1 w-40">
                            <option value="" selected>Todas</option>
                            <option v-for="conta in contas" :key="conta.id" :value="conta.id">{{ conta.descricao || conta.nome }}</option>
                        </select>
                    </div>
                    <div>
                        <label for="tipoTransacao" class="block text-sm font-medium text-gray-400">Tipo Transação</label>
                        <select id="tipoTransacao" v-model="tipoTransacaoSelecionada" @change="buscarLancamentos" class="border rounded px-2 py-1 w-40">
                            <option value="" selected>Todos</option>
                            <option v-for="tipo in tipoTransacoes" :key="tipo.id" :value="tipo.id">{{ tipo.descricao }}</option>
                        </select>
                    </div>                    
                </div>
            </AccordionTab>
        </Accordion>

        <div class="flex items-center gap-2 group-header-right p-2 m-2">
            <span class="total">Saldo inicial:  {{ formataValor(saldoInicial) }}</span>
        </div>        
        <DataTable 
            :value="lancamentos" 
            rowGroupMode="subheader" 
            sortMode="single" 
            groupRowsBy="dataTransacao" 
            sortField="dataTransacao" 
            :sortOrder="8" 
            stripedRows 
            scrollable 
            scrollHeight="600px" 
        >
            <template #groupfooter="slotProps">
                <div class="flex items-center gap-2 group-header-right">
                    <span class="group-header-small">
                        {{ slotProps.data.dataTransacao }} - {{ formataValor(somaPorData(slotProps.data.dataTransacao)) }}
                    </span>
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
            <span class="total">Saldo final:  {{ formataValor(saldoFinal) }}</span>
        </div>
    </div>
</template>

<script setup>
import { onBeforeMount, ref } from 'vue';
import { useToast } from 'primevue/usetoast';
import { getLancamentos, getCategorias, getTipoContas, getContas, getTipoTransacoes } from '../../../service/lancamentos/LancamentosService';
import formataValor from '@/helpers/formataValor';
const toast = useToast();
const lancamentos = ref([]);

// Filtros
const categorias = ref([]);
const tipoContas = ref([]);
const contas = ref([]);
const tipoTransacoes = ref([]);


// Data inicial e data final da exibição dos lançamentos
const hoje = new Date();
const primeiroDia = new Date(hoje.getFullYear(), hoje.getMonth(), 1);
const ultimoDia = new Date(hoje.getFullYear(), hoje.getMonth() + 1, 0);
function formatDate(date) { return date.toISOString().split('T')[0]; };
const dataInicial = ref(formatDate(primeiroDia));
const dataFinal = ref(formatDate(ultimoDia));

// Cálculo dos saldos
const saldoInicial = ref(10000000);
const saldoFinal = ref(0);
function somaPorData(dataTransacao) {
    if (!dataTransacao) return 0;
    // Soma acumulada até a data (inclusive)
    return lancamentos.value
        .filter(l => l.dataTransacao <= dataTransacao)
        .reduce((acc, l) => {
            const valorNum = Number(l.valor);
            return acc + (isNaN(valorNum) ? 0 : valorNum);
        }, 0);
}

// Requisição ao backend
async function buscarLancamentos() {
    try {
        const params = {
            dataInicial: dataInicial.value,
            dataFinal: dataFinal.value
        };
        lancamentos.value = await getLancamentos(params);

        let saldoTela = 0;
        lancamentos.value.forEach(lancamento => {
            console.log(lancamento.valor);
            saldoTela += Number(lancamento.valor);
        });
        saldoFinal.value = saldoInicial.value + saldoTela;

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

onBeforeMount(async () => {
    [categorias.value, tipoContas.value, contas.value, tipoTransacoes.value] = await Promise.all([
        getCategorias(),
        getTipoContas(),
        getContas(),
        getTipoTransacoes()
    ]);
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
