<script>
    import {HexagonIcon} from 'svelte-feather-icons';

    const services = [
        {
            icon: 'adjust-circle',
            title: 'Grow Your Business',
            description: "If the distribution of letters and 'words' is random, the reader will not be distracted from making.",
        },
        {
            icon: 'circuit',
            title: 'Drive More Sales',
            description: "If the distribution of letters and 'words' is random, the reader will not be distracted from making.",
        },
        {
            icon: 'fire',
            title: 'Handled By Expert',
            description: "If the distribution of letters and 'words' is random, the reader will not be distracted from making.",
        },
        {
            icon: 'flower',
            title: 'Increase Conversion',
            description: "If the distribution of letters and 'words' is random, the reader will not be distracted from making.",
        },
        {
            icon: 'shopping-basket',
            title: 'Drive More Sales',
            description: "If the distribution of letters and 'words' is random, the reader will not be distracted from making.",
        },
        {
            icon: 'flip-h',
            title: 'Sales Growth Idea',
            description: "If the distribution of letters and 'words' is random, the reader will not be distracted from making.",
        }
    ];

</script>
{#each services as service}
    <div class="group relative lg:px-6 transition duration-500 ease-in-out rounded-xl overflow-hidden text-center">
        <div class="relative overflow-hidden text-transparent -m-3">
            <HexagonIcon class="h-28 w-28 fill-violet-600/5 mx-auto rotate-[30deg]"
            ></HexagonIcon>
            <div class="absolute top-2/4 -translate-y-2/4 start-0 end-0 mx-auto text-violet-600 rounded-xl transition duration-500 ease-in-out text-3xl flex align-middle justify-center items-center">
                <i class={`uil uil-${service.icon}`}></i>
            </div>
        </div>
        <div class="mt-6">
            <a href="/services" class="text-lg h5 transition duration-500 ease-in-out hover:text-violet-600" >
                {service.title}
            </a>
            <p class="text-slate-400 transition duration-500 ease-in-out mt-3">
                {service.description}
            </p>
        </div>
    </div>
{/each}