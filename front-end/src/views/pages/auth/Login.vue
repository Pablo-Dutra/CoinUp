<template>
    <div class="bg-surface-50 dark:bg-surface-950 flex items-center justify-center min-h-screen min-w-[100vw] overflow-hidden">
        <div class="flex flex-col items-center justify-center">
            <div style="border-radius: 56px; padding: 0.3rem; background: linear-gradient(180deg, var(--primary-color) 10%, rgba(33, 150, 243, 0) 30%)">
                <div class="w-full bg-surface-0 dark:bg-surface-900 py-20 px-8 sm:px-20" style="border-radius: 53px">
                    <div class="text-center mb-8">
                        <div class="text-surface-900 dark:text-surface-0 text-3xl font-medium mb-4"><div class="pi pi-bitcoin"></div> Coin UP</div>
                        <span class="text-muted-color font-medium">Faça login para continuar</span>
                    </div>
                    <div>
                        <form @submit.prevent="handleLogin">
                            <InputText id="email" type="text" placeholder="e-mail" class="w-full md:w-[30rem] mb-8" v-model="email" required />
                            <Password id="password" v-model="password" placeholder="senha" :toggleMask="true" class="mb-4" fluid :feedback="false" required />
                            <Button label="Entrar" type="submit" class="w-full"><i class="pi pi-bitcoin"></i> Entrar</Button>
                        </form>
                        <div v-if="error" class="error">{{ error }}</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios';
const email = ref('');
const password = ref('');
const error = ref('');
const router = useRouter();

const handleLogin = async () => {
    try {
        const params = new URLSearchParams();
        params.append('grant_type', 'password');
        params.append('username', email.value);
        params.append('password', password.value);
        params.append('scope', '');
        params.append('client_id', 'string');
        params.append('client_secret', '********');

        const response = await axios.post('http://127.0.0.1:8000/login', params, {
            headers: {
                accept: 'application/json',
                'Content-Type': 'application/x-www-form-urlencoded'
            }
        });

        if (response.status == 200) {
            const { access_token, token_type } = response.data;
            sessionStorage.setItem('access_token', access_token);
            sessionStorage.setItem('token_type', token_type);
            sessionStorage.setItem('username', email.value);
            router.push('/lancamentos');
        } else {
            error.value = 'Login failed. Please check your credentials.';
            console.error('Response:', response.data.message);
        }
    } catch (err) {
        console.error('Error during login:', err);
    } finally {
        // Clean up or finalize any actions
    }
};
</script>

<style scoped>
.pi-eye {
    transform: scale(1.6);
    margin-right: 1rem;
}

.pi-eye-slash {
    transform: scale(1.6);
    margin-right: 1rem;
}
</style>
