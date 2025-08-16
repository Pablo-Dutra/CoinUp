<template>
    <ul class="layout-menu">
        <template v-for="(item, i) in model" :key="item">
            <app-menu-item v-if="!item.separator" :item="item" :index="i"></app-menu-item>
            <li v-if="item.separator" class="menu-separator"></li>
        </template>
    </ul>
</template>
<script setup>
import { ref } from 'vue';

import AppMenuItem from './AppMenuItem.vue';

const model = ref([
    {
        label: 'Home',
        items: [{ label: 'Lançamentos', icon: 'pi pi-fw pi-dollar', to: '/lancamentos' }]
    },
    {
        label: 'Módulos',
        items: [
            { label: 'Contas', icon: 'pi pi-fw pi-credit-card', to: '/contas' },
            { label: 'Categorias', icon: 'pi pi-fw pi-image', to: '/categorias' },
            { label: 'Gráficos', icon: 'pi pi-fw pi-chart-line', to: '/graficos' },
        ]
    },
    {
        label: 'Arquivos',
        items: [
            { label: 'Importação', icon: 'pi pi-fw pi-download', to: '/importacoes' },
            { label: 'Exportação', icon: 'pi pi-fw pi-upload', to: '/exportacoes' },
        ]
    }
]);
</script>



<style lang="scss" scoped></style>
