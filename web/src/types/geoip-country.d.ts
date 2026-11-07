declare module "geoip-country" {
  interface GeoCountry {
    country: string;
  }
  const geoip: { lookup(ip: string): GeoCountry | null };
  export default geoip;
}
