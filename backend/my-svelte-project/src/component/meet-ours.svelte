<script>
    import image from '../assets/images/client/04.jpg';
import image1 from '../assets/images/client/05.jpg';
import image2 from '../assets/images/client/06.jpg';
import image3 from '../assets/images/client/07.jpg';
import { FacebookIcon , InstagramIcon, LinkedinIcon } from 'svelte-feather-icons';

const MeetOursdata = [
        {
            image: image,
            title: 'Jack John',
            type: 'Designer'
        },
        {
            image: image1,
            title: 'Krista John',
            type: 'Designer'
        },
        {
            image: image2,
            title: 'Roger Jackson',
            type: 'Designer'
        },
        {
            image: image3,
            title: 'Johnny English',
            type: 'Designer'
        },
    ]
</script>
<div class="container lg:mt-24 mt-16">
    <div class="grid grid-cols-1 pb-8 text-center">
        <h3 class="mb-4 md:text-2xl text-xl font-medium">Meet Our Teammates</h3>
        <p class="text-slate-400 max-w-xl mx-auto">This is just a simple text made for this unique and awesome
            template, you can replace it with any text.</p>
    </div>
    <div class="grid md:grid-cols-12 grid-cols-1 mt-8 gap-[30px]">
        {#each MeetOursdata as item}
            <div class="lg:col-span-3 md:col-span-6">
                <div class="group text-center">
                    <div class="relative inline-block mx-auto h-52 w-52 rounded-full overflow-hidden">
                        <img src={item.image} class="" alt="" />
                        <ul
                            class="list-none absolute top-1/2 -translate-y-1/2 -end-20 group-hover:end-5 transition-all duration-500 ease-in-out">
                            <li class=""><a href="/"
                                class="h-8 w-8 inline-flex items-center text-center justify-center text-base font-normal tracking-wide border align-middle transition duration-500 ease-in-out rounded-full bg-violet-600 hover:bg-violet-700 border-violet-600 hover:border-violet-700 text-white"><FacebookIcon class="h-4 w-4"></FacebookIcon></a></li>
                            <li class="mt-1"><a href="/"
                                class="h-8 w-8 inline-flex items-center text-center justify-center text-base font-normal tracking-wide border align-middle transition duration-500 ease-in-out rounded-full bg-violet-600 hover:bg-violet-700 border-violet-600 hover:border-violet-700 text-white"><InstagramIcon class="h-4 w-4"></InstagramIcon></a></li>
                            <li class="mt-1"><a href="/"
                                class="h-8 w-8 inline-flex items-center text-center justify-center text-base font-normal tracking-wide border align-middle transition duration-500 ease-in-out rounded-full bg-violet-600 hover:bg-violet-700 border-violet-600 hover:border-violet-700 text-white"><LinkedinIcon class="h-4 w-4"></LinkedinIcon></a></li>
                        </ul>
                    </div>

                    <div class="content mt-3">
                        <a href="/"
                            class="text-lg hover:text-violet-600 transition-all duration-500 ease-in-out h5">{item.title}</a>
                        <p class="text-slate-400">{item.type}</p>
                    </div>
                </div>
            </div>
        {/each}
    </div>
</div>