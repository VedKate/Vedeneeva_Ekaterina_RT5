class Urls {
    constructor() {
        this.url = 'http://localhost:65415/';
    }

    stocks() {
        return `${this.url}Streets/`
    }

    stock(id) {
        return `${this.url}Streets/${id}/`
    }
}

export const urls = new Urls()