<script>
    import {HexagonIcon} from 'svelte-feather-icons';

    const ContactData = [
        {
            icon: 'uil uil-phone',
            title: 'Phone',
            detail: 'The phrasal sequence of the is now so that many campaign and benefit',
            type: '+152 534-468-854'
        },
        {
            icon: 'uil uil-envelope',
            title: 'Email',
            detail: 'The phrasal sequence of the is now so that many campaign and benefit',
            type: 'contact@example.com'
        },
        {
            icon: 'uil uil-map-marker',
            title: 'Location',
            detail: 'C/54 Northwest Freeway, Suite 558, Houston, USA 485',
            type: 'View on Google map'
        }
    ]
</script>
<div class="container lg:mt-24 mt-16">
    <div class="grid grid-cols-1 lg:grid-cols-3 md:grid-cols-2 gap-[30px]">
        {#each ContactData as item}
            <div class="text-center px-6">
                <div class="relative overflow-hidden text-transparent -m-3">
                    <HexagonIcon class="h-28 w-28 fill-violet-600/5 mx-auto rotate-[30deg]"></HexagonIcon>
                    <div class="absolute top-2/4 -translate-y-2/4 start-0 end-0 mx-auto text-violet-600 rounded-xl transition-all duration-500 ease-in-out text-4xl flex align-middle justify-center items-center">
                        <i class={item.icon}></i>
                    </div>
                </div>

                <div class="content mt-7">
                    <h5 class="title h5 text-xl font-medium">{item.title}</h5>
                    <p class="text-slate-400 mt-3">{item.detail}</p>

                    <div class="mt-5">
                        <a href="tel:+152534-468-854" class="text-violet-600 hover:text-violet-600 after:bg-violet-600 transition duration-500">{item.type}</a>
                    </div>
                </div>
            </div>
        {/each}
    </div>
</div>
