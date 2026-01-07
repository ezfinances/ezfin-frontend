/**
 * Serviço de API para comunicação com o backend.
 * Configuração base e métodos HTTP.
 */

// Detectar automaticamente qual URL usar baseado no ambiente
const determineApiUrl = () => {
  const hostname = window.location.hostname;
  
  // Se estiver em produção (Fly.io), usar a URL de produção
  if (hostname.includes('fly.dev') || hostname === 'ezfin-frontend.fly.dev') {
    return 'https://ezfin-backend.fly.dev';
  }
  
  // Se estiver em localhost, usar localhost
  if (hostname === 'localhost' || hostname === '127.0.0.1') {
    return 'http://localhost:8000';
  }
  
  // Fallback para variável de ambiente (buildtime)
  return process.env.REACT_APP_API_URL || 'http://localhost:8000';
};

const API_BASE_URL = determineApiUrl();

// Log para debug (remover em produção se necessário)
console.log('[API] Hostname:', window.location.hostname, '| API URL:', API_BASE_URL);

class ApiService {
  constructor(baseURL = API_BASE_URL) {
    this.baseURL = baseURL;
  }

  /**
   * Faz requisição GET
   */
  async get(endpoint) {
    const token = localStorage.getItem('token');
    const headers = {
      'Content-Type': 'application/json',
    };
    if (token) {
      headers['Authorization'] = `Bearer ${token}`;
    }

    try {
      const response = await fetch(`${this.baseURL}${endpoint}`, {
        method: 'GET',
        headers,
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      return response.json();
    } catch (error) {
      if (error instanceof TypeError) {
        throw new Error(`Erro de conexão com o servidor (${this.baseURL}). Verifique se o backend está disponível.`);
      }
      throw error;
    }
  }

  /**
   * Faz requisição POST
   */
  async post(endpoint, data) {
    const token = localStorage.getItem('token');
    const headers = {
      'Content-Type': 'application/json',
    };
    if (token) {
      headers['Authorization'] = `Bearer ${token}`;
    }

    try {
      const response = await fetch(`${this.baseURL}${endpoint}`, {
        method: 'POST',
        headers,
        body: JSON.stringify(data),
      });

      if (!response.ok) {
        let errorData = {};
        try {
          errorData = await response.json();
        } catch (e) {
          // Se não conseguir fazer parse do JSON, continua sem dados de erro
        }
        
        let errorMessage = `HTTP error! status: ${response.status}`;
        
        // Handle Pydantic validation errors (array of objects)
        if (Array.isArray(errorData.detail)) {
          errorMessage = errorData.detail
            .map(err => `${err.loc?.[err.loc.length - 1] || 'campo'}: ${err.msg}`)
            .join('; ');
        } else if (typeof errorData.detail === 'string') {
          errorMessage = errorData.detail;
        }
        
        throw new Error(errorMessage);
      }
      return response.json();
    } catch (error) {
      if (error instanceof TypeError) {
        throw new Error(`Erro de conexão com o servidor (${this.baseURL}). Verifique se o backend está disponível.`);
      }
      throw error;
    }
  }

  /**
   * Faz requisição PUT
   */
  async put(endpoint, data) {
    const token = localStorage.getItem('token');
    const headers = {
      'Content-Type': 'application/json',
    };
    if (token) {
      headers['Authorization'] = `Bearer ${token}`;
    }

    try {
      const response = await fetch(`${this.baseURL}${endpoint}`, {
        method: 'PUT',
        headers,
        body: JSON.stringify(data),
      });

      if (!response.ok) {
        let errorData = {};
        try {
          errorData = await response.json();
        } catch (e) {
          // Se não conseguir fazer parse do JSON, continua sem dados de erro
        }
        
        let errorMessage = `HTTP error! status: ${response.status}`;
        
        // Handle Pydantic validation errors (array of objects)
        if (Array.isArray(errorData.detail)) {
          errorMessage = errorData.detail
            .map(err => `${err.loc?.[err.loc.length - 1] || 'campo'}: ${err.msg}`)
            .join('; ');
        } else if (typeof errorData.detail === 'string') {
          errorMessage = errorData.detail;
        }
        
        throw new Error(errorMessage);
      }
      return response.json();
    } catch (error) {
      if (error instanceof TypeError) {
        throw new Error(`Erro de conexão com o servidor (${this.baseURL}). Verifique se o backend está disponível.`);
      }
      throw error;
    }
  }

  /**
   * Faz requisição DELETE
   */
  async delete(endpoint) {
    const token = localStorage.getItem('token');
    const headers = {
      'Content-Type': 'application/json',
    };
    if (token) {
      headers['Authorization'] = `Bearer ${token}`;
    }

    try {
      const response = await fetch(`${this.baseURL}${endpoint}`, {
        method: 'DELETE',
        headers,
      });

      if (!response.ok) {
        let errorMessage = `HTTP error! status: ${response.status}`;
        
        try {
          const errorData = await response.json();
          if (errorData.detail) {
            errorMessage = errorData.detail;
          }
        } catch (e) {
          // Se não conseguir fazer parse do JSON, usa apenas o status
          console.error('Erro ao fazer parse da resposta de erro:', e);
        }
        
        throw new Error(errorMessage);
      }
      
      // Trata resposta com status 200 (com conteúdo JSON) ou 204 (sem conteúdo)
      if (response.status === 204) {
        return null;
      }
      
      const contentType = response.headers.get('content-type');
      if (contentType && contentType.includes('application/json')) {
        return await response.json();
      }
      
      return null;
    } catch (error) {
      if (error instanceof TypeError) {
        // Erro de conexão/rede
        throw new Error('Erro de conexão com o servidor. Verifique se o backend está disponível.');
      }
      throw error;
    }
  }
}

export default new ApiService();
