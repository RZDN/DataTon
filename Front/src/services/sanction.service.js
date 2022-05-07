import axios from "axios";
const API_URL = 'http://127.0.0.1:4000';

class SanctionService{
    getAllSanctionsByRuc(ruc){
        return axios.get(API_URL+`/empresas/${ruc}/sanciones`)
    }
}

export default new SanctionService();
