const inputPrompt = require("../models/input-prompt");
const openai = require("../config/openai");

module.exports = {
    async sendText(req, res) {

        const inputModel = new inputPrompt(req.body);

       // Substitua o try/catch atual por este para isolar o problema:
try {
    // Pegue o texto diretamente, sem passar pelo inputPrompt por enquanto
    const promptText = req.body.prompt || req.body.message; 
    
    const response = await openai.textCompletion({ prompt: promptText });

    return res.status(200).json({
        sucess: true,
        data: response 
    });
} catch (error) {
    // Esse log vai te mostrar EXATAMENTE o que a OpenAI respondeu
    console.log("ERRO DETALHADO:", error.response?.data || error.message);
    
    return res.status(400).json({
        sucess: false,
        error: error.message
    });
}
    }
};