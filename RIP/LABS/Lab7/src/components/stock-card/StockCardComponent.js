export class StockCardComponent {
    constructor(parent) {
        this.parent = parent;
    }
    getHTML(data) {
        return (
            `
                <div class="card" style="width: 300px;">
                    
                    <div class="card-body">
                        <h5 class="card-title">${data.StreetName}</h5>
                        <p class="card-text">${data.City}</p>
                        <button class="btn btn-primary" id="click-card-${data.idStreet}" data-id="${data.idStreet}">Нажми на меня</button>

                    </div>
                </div>
            `
        )
    }

    addListeners(data, listener) {
        document
            .getElementById(`click-card-${data.pk}`)
            .addEventListener("click", listener)
    }

    render(data, listener) {
        const html = this.getHTML(data)
        this.parent.insertAdjacentHTML('beforeend', html)
        this.addListeners(data, listener)
    }
}