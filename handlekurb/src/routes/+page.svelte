<script lang="ts">
    import { localStorageStore } from "@skeletonlabs/skeleton"
      import type { Writable } from 'svelte/store';

    interface vare {
        name: string
        status: any
    }

    const vareStore: Writable<vare[]> = localStorageStore("vareStore",[]);
	
    let inputVare = "";
    let inputState = false;

    const addToList = () => {
        $vareStore = [
            {
                name: inputVare,
                status: inputState,
            },
            ...$vareStore
        ];
        
        inputVare = "";
        inputState = false;
    }
    const removeFromList = (index: Number) => {
        $vareStore = $vareStore.filter((vare,vareIndex) => vareIndex !== index)
    }

</script>


<head>
    <title>Aksels amazing handle liste</title>
</head>

<body>
    <section>

        <h1>
            HandleListe
        </h1>
        <div>
            <form>
                <input bind:value={inputVare} type="text" placeholder="Legg til i handle kurven" style="color: black;">
                <button on:click={addToList}>Legg til</button>
            </form>
        </div>

        <article>
            {#each $vareStore as vare, index}
                <input bind:checked={vare.status} type="checkbox">
                <span class:checked={vare.status}>{vare.name}</span>
                <!-- svelte-ignore a11y-click-events-have-key-events -->
                <!-- svelte-ignore a11y-no-static-element-interactions -->
                <span on:click={() => removeFromList(index)}>❌</span>
                <br/>
            {/each}
        </article>
    </section>
</body>

