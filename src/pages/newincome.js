function NewIncome() {
    return (
            <div className="flex flex-col items-center justify-center gap-4 bg-green-500">
                
                <div className="bg-white backdrop-blur-sm shadow-lg rounded-lg p-8 w-[400px]">
                    <div className="mb-4">
                        <h1 className="text-2xl font-semibold text-gray-800 flex justify-center">Nova Renda extra</h1>
                    </div>
                    
                    <label className="block text-lg font-semibold text-[#000] mb-1">Conta Bancária</label>
                    <select className="w-full px-3 py-2 mb-2 border border-gray-200 rounded-lg bg-white focus:outline-none focus:ring-2 focus:ring-[#171717]">
                        <option value="">Selecione a Conta Bancária</option>
                        <option value="nubank">Nubank</option>
                        <option value="inter">Banco Inter</option>
                        <option value="bb">Banco do Brasil</option>
                        <option value="caixa">Caixa</option>
                    </select>
                    <label className="block text-lg font-semibold text-[#000] mb-1">Nome da renda</label>
                    <input className="w-full px-4 py-2 mb-2 border border-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#171717]" type="text" placeholder="Digite o nome da renda" />
                    <label className="block text-lg font-semibold text-[#000] mb-1">Valor</label>
                    
                    <input className="w-full px-4 py-2 mb-6 border border-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#171717]" type="number" placeholder="Digite o valor" />
                    <div className="flex gap-4 justify-end">
                        <button className="w-full bg-red-100 text-red-400 font-semibold py-2 rounded-lg hover:bg-red-300 hover:text-red-500 transition">Cancelar</button>
                        <button className="w-full bg-[#171717] text-white py-2 font-semibold rounded-lg hover:bg-[#000] transition">Salvar</button>
                    </div>
                    
                </div>
            </div>
    );
}

export default NewIncome;