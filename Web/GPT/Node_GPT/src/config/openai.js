const OpenAI = require('openai');
require('dotenv').config(); // Garante que as variáveis do .env sejam carregadas aqui dentro

module.exports = class openai {
    
    static configuration() {
        // Se a variável sumir de novo, o console.log vai te avisar no terminal
        if (!process.env.OPENAI_API_KEY) {
            console.error("ERRO: A chave OPENAI_API_KEY não foi encontrada no .env!");
        }

        return new OpenAI({
            apiKey: process.env.OPENAI_API_KEY
        });
    }

    static async textCompletion({ prompt }) {
        const openai = this.configuration();

        try {
            const response = await openai.chat.completions.create({
                model: "gpt-4o-mini",
                messages: [
                    { role: "user", content: prompt }
                ],
                temperature: 0,
                max_tokens: 256,
            });

            return response.choices[0].message.content; 
        } catch (error) {
            // Lança o erro para o controller tratar
            throw error;
        }
    }
}