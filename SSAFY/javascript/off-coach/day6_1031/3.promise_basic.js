const myPromise = new Promise((resolve, reject) => {
    console.log('Promise 생성됨')

    let num = 1
    if (num === 0) {
        resolve('성공')
    } else {
        reject('로직 수행 실패')
    }
    // if 문 없이 그냥 쓰면 더 위에 있는 것이 호출됩니다
})

myPromise
.then((result) => {
    console.log(result)
})
.catch((error) => {
    console.log(`error = ${error}`)
})