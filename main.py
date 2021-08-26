
<div class='container'>
    <div class="row">
        <div class="col-md-12">
            <div class="col-md-4">
                {% for content in '01234'|make_list %}
                <div class="list-group my-1">
                    <a href="#" class="list-group-item list-group-item-action flex-column align-items-start active">
                        <div class="d-flex w-100 justify-content-between">
                            <h5 class="mb-1">List group item heading</h5>
                            <small>3 days ago</small>
                        </div>
                        <p class="mb-1">Donec id elit non mi porta gravida at eget metus. Maecenas sed diam eget risus
                            varius
                            blandit.</p>
                        <small>Donec id elit non mi porta.</small>
                    </a>
                    {% endfor %}
                </div>
            </div>
        </div>
    </div>
</div>