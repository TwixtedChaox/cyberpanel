document.addEventListener('DOMContentLoaded', function () {
    new Vue({
        el: '#emailAliasApp',
        delimiters: ['[[', ']]'],
        data: {
            aliases: [],
            newSource: '',
            newDestination: '',
            error: '',
            success: ''
        },
        methods: {
            fetchAliases() {
                fetch('fetch/', {method: 'POST'})
                    .then(r => r.json())
                    .then(data => { this.aliases = data.aliases; });
            },
            addAlias() {
                this.error = '';
                this.success = '';
                fetch('add/', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({source: this.newSource, destination: this.newDestination})
                }).then(r => r.json()).then(data => {
                    if (data.status) {
                        this.success = data.message;
                        this.newDestination = '';
                        this.fetchAliases();
                    } else {
                        this.error = data.error;
                    }
                });
            },
            deleteAlias(src, dst) {
                fetch('delete/', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({source: src, destination: dst})
                }).then(() => this.fetchAliases());
            }
        },
        mounted() {
            this.fetchAliases();
        }
    });
});
