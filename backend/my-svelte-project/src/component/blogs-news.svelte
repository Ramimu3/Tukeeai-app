<script>
    import image from '../assets/images/blog/1.jpg';
    import image1 from '../assets/images/blog/2.jpg';
    import image2 from '../assets/images/blog/3.jpg';
    const BlogsNewsdata = [
        {
            image: image,
            title: 'Introducing new tools for your design.',
            detail: 'The phrasal sequence of the is now so that many campaign and benefit',
            more: 'Read More',
        },
        {
            image: image1,
            title: 'The Right Hand of Business IT World',
            detail: 'The phrasal sequence of the is now so that many campaign and benefit',
            more: 'Read More',
        },
        {
            image: image2,
            title: 'Truck Side Advertising Isn It Time for action.',
            detail: 'The phrasal sequence of the is now so that many campaign and benefit',
            more: 'Read More',
        }

    ];
</script>
<section class="container lg:py-24 py-16" id="blog">
    <div class="grid grid-cols-1 pb-8 text-center">
        <h3 class="mb-4 md:text-2xl text-xl font-medium">Blogs or News</h3>

        <p class="text-slate-400 dark:text-slate-300 max-w-xl mx-auto">Launch your campaign and benefit from our expertise on designing and managing conversion centered Tailwind CSS html page.</p>
    </div>

    <div class="grid grid-cols-1 lg:grid-cols-3 md:grid-cols-2 gap-[30px] mt-8">
        {#each BlogsNewsdata as item}
            <div class="blog relative rounded-md shadow shadow-slate-200 dark:shadow-gray-800 overflow-hidden">
                <img src={item.image} alt="" />

                <div class="content p-6">
                    <a href="/blog-detail" class="text-lg hover:text-violet-600 dark:text-white dark:hover:text-violet-600 transition duration-500 ease-in-out font-medium h5">{item.title}</a>
                    <p class="text-slate-400 mt-3">{item.detail}</p>

                    <div class="mt-5">
                        <a href="/blog-detail" class="hover:text-violet-600 dark:hover:text-violet-600 after:bg-violet-600 dark:text-white transition duration-500">{item.more}<i class="uil uil-arrow-right"></i></a>
                    </div>
                </div>
            </div>
        {/each}
    </div>
</section>
